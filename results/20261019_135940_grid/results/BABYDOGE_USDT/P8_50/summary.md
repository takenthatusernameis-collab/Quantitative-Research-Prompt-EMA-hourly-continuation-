# EMA Hourly Continuation — BABYDOGE/USDT P8_50

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 82 |
| net_profit_factor | 0.9168 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9922 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.2243 |
| sortino_ratio | -0.0290 |
| max_drawdown | 0.0880 |
| cagr | -0.0143 |
| net_avg_win | 96.2040 |
| net_avg_loss | -104.9290 |
| avg_hold_time_bars | 28.7195 |
| exposure | 0.1066 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
