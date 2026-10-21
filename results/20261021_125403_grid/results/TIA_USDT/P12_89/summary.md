# EMA Hourly Continuation — TIA/USDT P12_89

**Symbol:** TIA/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.9261 |
| net_win_rate | 0.5233 |
| gross_profit_factor | 1.0820 |
| gross_win_rate | 0.5233 |
| sharpe_ratio | -0.4694 |
| sortino_ratio | -0.1468 |
| max_drawdown | 0.3233 |
| cagr | -0.0710 |
| net_avg_win | 85.5988 |
| net_avg_loss | -101.4717 |
| avg_hold_time_bars | 24.7161 |
| exposure | 0.5303 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
