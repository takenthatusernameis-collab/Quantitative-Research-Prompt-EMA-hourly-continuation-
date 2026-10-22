# EMA Hourly Continuation — STX/USDT P55_144

**Symbol:** STX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 454 |
| net_profit_factor | 0.5915 |
| net_win_rate | 0.4824 |
| gross_profit_factor | 0.9112 |
| gross_win_rate | 0.4890 |
| sharpe_ratio | -3.1947 |
| sortino_ratio | -0.9469 |
| max_drawdown | 0.6921 |
| cagr | -0.3686 |
| net_avg_win | 45.3977 |
| net_avg_loss | -71.5210 |
| avg_hold_time_bars | 12.1432 |
| exposure | 0.2495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
