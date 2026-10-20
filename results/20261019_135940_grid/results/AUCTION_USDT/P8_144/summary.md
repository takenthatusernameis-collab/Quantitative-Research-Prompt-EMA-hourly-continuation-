# EMA Hourly Continuation — AUCTION/USDT P8_144

**Symbol:** AUCTION/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 471 |
| net_profit_factor | 0.6212 |
| net_win_rate | 0.4522 |
| gross_profit_factor | 0.8909 |
| gross_win_rate | 0.4692 |
| sharpe_ratio | -3.6057 |
| sortino_ratio | -1.0928 |
| max_drawdown | 0.7427 |
| cagr | -0.4102 |
| net_avg_win | 56.6472 |
| net_avg_loss | -75.2906 |
| avg_hold_time_bars | 35.8089 |
| exposure | 0.7633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
