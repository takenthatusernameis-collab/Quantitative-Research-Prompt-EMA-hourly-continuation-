# EMA Hourly Continuation — CARV/USDT P12_200

**Symbol:** CARV/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 392 |
| net_profit_factor | 0.5846 |
| net_win_rate | 0.4515 |
| gross_profit_factor | 0.8270 |
| gross_win_rate | 0.4541 |
| sharpe_ratio | -3.5761 |
| sortino_ratio | -1.1034 |
| max_drawdown | 0.6805 |
| cagr | -0.4082 |
| net_avg_win | 52.0732 |
| net_avg_loss | -73.3322 |
| avg_hold_time_bars | 30.4796 |
| exposure | 0.6724 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
