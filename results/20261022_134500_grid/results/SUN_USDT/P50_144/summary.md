# EMA Hourly Continuation — SUN/USDT P50_144

**Symbol:** SUN/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.3797 |
| net_win_rate | 0.3884 |
| gross_profit_factor | 0.8281 |
| gross_win_rate | 0.4209 |
| sharpe_ratio | -6.8583 |
| sortino_ratio | -1.9911 |
| max_drawdown | 0.9321 |
| cagr | -0.6531 |
| net_avg_win | 34.1115 |
| net_avg_loss | -57.0519 |
| avg_hold_time_bars | 15.8093 |
| exposure | 0.3076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
