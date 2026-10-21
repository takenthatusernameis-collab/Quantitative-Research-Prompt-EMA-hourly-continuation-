# EMA Hourly Continuation — FLOW/USDT P55_100

**Symbol:** FLOW/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.6758 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9240 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -2.2044 |
| sortino_ratio | -0.5931 |
| max_drawdown | 0.5082 |
| cagr | -0.2383 |
| net_avg_win | 60.3539 |
| net_avg_loss | -83.9148 |
| avg_hold_time_bars | 7.6176 |
| exposure | 0.1222 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
