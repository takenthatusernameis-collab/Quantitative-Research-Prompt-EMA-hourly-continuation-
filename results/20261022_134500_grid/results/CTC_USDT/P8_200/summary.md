# EMA Hourly Continuation — CTC/USDT P8_200

**Symbol:** CTC/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.5841 |
| net_win_rate | 0.4559 |
| gross_profit_factor | 0.8846 |
| gross_win_rate | 0.4600 |
| sharpe_ratio | -3.9371 |
| sortino_ratio | -1.2125 |
| max_drawdown | 0.8035 |
| cagr | -0.4502 |
| net_avg_win | 49.1696 |
| net_avg_loss | -70.5252 |
| avg_hold_time_bars | 34.2341 |
| exposure | 0.7578 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
