# EMA Hourly Continuation — ENS/USDT P144_200

**Symbol:** ENS/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.3453 |
| net_win_rate | 0.4132 |
| gross_profit_factor | 0.7070 |
| gross_win_rate | 0.4279 |
| sharpe_ratio | -5.9988 |
| sortino_ratio | -1.7230 |
| max_drawdown | 0.8865 |
| cagr | -0.5780 |
| net_avg_win | 27.6391 |
| net_avg_loss | -56.3568 |
| avg_hold_time_bars | 3.8680 |
| exposure | 0.0719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
