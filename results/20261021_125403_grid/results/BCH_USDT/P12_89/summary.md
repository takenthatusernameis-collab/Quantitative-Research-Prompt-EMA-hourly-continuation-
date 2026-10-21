# EMA Hourly Continuation — BCH/USDT P12_89

**Symbol:** BCH/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 478 |
| net_profit_factor | 0.7331 |
| net_win_rate | 0.4812 |
| gross_profit_factor | 0.9569 |
| gross_win_rate | 0.4812 |
| sharpe_ratio | -2.3841 |
| sortino_ratio | -0.7443 |
| max_drawdown | 0.6061 |
| cagr | -0.2891 |
| net_avg_win | 68.7288 |
| net_avg_loss | -86.9453 |
| avg_hold_time_bars | 21.8661 |
| exposure | 0.4751 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
