# EMA Hourly Continuation — COMP/USDT P34_200

**Symbol:** COMP/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 402 |
| net_profit_factor | 0.5817 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.8883 |
| gross_win_rate | 0.4826 |
| sharpe_ratio | -2.9517 |
| sortino_ratio | -0.8336 |
| max_drawdown | 0.6392 |
| cagr | -0.3269 |
| net_avg_win | 46.0984 |
| net_avg_loss | -71.0287 |
| avg_hold_time_bars | 28.4080 |
| exposure | 0.5191 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
