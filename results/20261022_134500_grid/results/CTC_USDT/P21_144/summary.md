# EMA Hourly Continuation — CTC/USDT P21_144

**Symbol:** CTC/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 575 |
| net_profit_factor | 0.6121 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.9531 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -3.7828 |
| sortino_ratio | -1.2748 |
| max_drawdown | 0.8142 |
| cagr | -0.4596 |
| net_avg_win | 46.1558 |
| net_avg_loss | -66.2863 |
| avg_hold_time_bars | 19.8000 |
| exposure | 0.5175 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
