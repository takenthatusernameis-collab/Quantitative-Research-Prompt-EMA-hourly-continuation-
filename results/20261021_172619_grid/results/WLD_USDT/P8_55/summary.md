# EMA Hourly Continuation — WLD/USDT P8_55

**Symbol:** WLD/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.9446 |
| net_win_rate | 0.5305 |
| gross_profit_factor | 1.1208 |
| gross_win_rate | 0.5305 |
| sharpe_ratio | -0.3981 |
| sortino_ratio | -0.1395 |
| max_drawdown | 0.3455 |
| cagr | -0.0702 |
| net_avg_win | 90.9926 |
| net_avg_loss | -108.8503 |
| avg_hold_time_bars | 18.7780 |
| exposure | 0.5036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
