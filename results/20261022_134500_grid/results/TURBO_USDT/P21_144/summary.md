# EMA Hourly Continuation — TURBO/USDT P21_144

**Symbol:** TURBO/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 444 |
| net_profit_factor | 0.7067 |
| net_win_rate | 0.4775 |
| gross_profit_factor | 0.9532 |
| gross_win_rate | 0.4820 |
| sharpe_ratio | -2.9028 |
| sortino_ratio | -0.9429 |
| max_drawdown | 0.6515 |
| cagr | -0.3604 |
| net_avg_win | 69.0583 |
| net_avg_loss | -89.2918 |
| avg_hold_time_bars | 21.6284 |
| exposure | 0.5239 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
