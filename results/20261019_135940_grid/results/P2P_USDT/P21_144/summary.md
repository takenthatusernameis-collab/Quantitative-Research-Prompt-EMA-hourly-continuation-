# EMA Hourly Continuation — P2P/USDT P21_144

**Symbol:** P2P/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 534 |
| net_profit_factor | 0.5553 |
| net_win_rate | 0.4232 |
| gross_profit_factor | 0.7201 |
| gross_win_rate | 0.4251 |
| sharpe_ratio | -3.8888 |
| sortino_ratio | -1.2601 |
| max_drawdown | 0.7893 |
| cagr | -0.4498 |
| net_avg_win | 42.9269 |
| net_avg_loss | -56.7258 |
| avg_hold_time_bars | 19.3989 |
| exposure | 0.4709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
