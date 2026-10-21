# EMA Hourly Continuation — MASK/USDT P34_55

**Symbol:** MASK/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 418 |
| net_profit_factor | 0.5597 |
| net_win_rate | 0.4737 |
| gross_profit_factor | 0.8745 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -3.5633 |
| sortino_ratio | -1.0398 |
| max_drawdown | 0.7158 |
| cagr | -0.3851 |
| net_avg_win | 45.2615 |
| net_avg_loss | -72.7865 |
| avg_hold_time_bars | 6.1555 |
| exposure | 0.1170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
