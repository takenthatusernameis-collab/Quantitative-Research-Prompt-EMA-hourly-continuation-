# EMA Hourly Continuation — PYTH/USDT P8_89

**Symbol:** PYTH/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 721 |
| net_profit_factor | 0.6541 |
| net_win_rate | 0.4799 |
| gross_profit_factor | 0.9285 |
| gross_win_rate | 0.4813 |
| sharpe_ratio | -3.6042 |
| sortino_ratio | -1.3574 |
| max_drawdown | 0.8154 |
| cagr | -0.4795 |
| net_avg_win | 44.0432 |
| net_avg_loss | -62.1305 |
| avg_hold_time_bars | 19.4466 |
| exposure | 0.6373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
