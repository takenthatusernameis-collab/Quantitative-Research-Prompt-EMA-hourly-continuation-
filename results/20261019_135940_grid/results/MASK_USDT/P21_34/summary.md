# EMA Hourly Continuation — MASK/USDT P21_34

**Symbol:** MASK/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1147 |
| net_profit_factor | 0.2562 |
| net_win_rate | 0.3906 |
| gross_profit_factor | 0.6966 |
| gross_win_rate | 0.4281 |
| sharpe_ratio | -12.1880 |
| sortino_ratio | -5.9121 |
| max_drawdown | 0.9995 |
| cagr | -0.9529 |
| net_avg_win | 7.6861 |
| net_avg_loss | -19.2256 |
| avg_hold_time_bars | 3.0235 |
| exposure | 0.1576 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
