# EMA Hourly Continuation — IO/USDT P20_144

**Symbol:** IO/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 333 |
| net_profit_factor | 0.7801 |
| net_win_rate | 0.4745 |
| gross_profit_factor | 0.9069 |
| gross_win_rate | 0.4745 |
| sharpe_ratio | -1.5015 |
| sortino_ratio | -0.4024 |
| max_drawdown | 0.3784 |
| cagr | -0.1700 |
| net_avg_win | 79.8163 |
| net_avg_loss | -92.3800 |
| avg_hold_time_bars | 35.7387 |
| exposure | 0.5762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
