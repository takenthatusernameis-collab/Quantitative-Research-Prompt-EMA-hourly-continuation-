# EMA Hourly Continuation — CRO/USDT P34_200

**Symbol:** CRO/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.5461 |
| net_win_rate | 0.4763 |
| gross_profit_factor | 0.9429 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -2.9641 |
| sortino_ratio | -0.7376 |
| max_drawdown | 0.6301 |
| cagr | -0.3031 |
| net_avg_win | 47.4981 |
| net_avg_loss | -79.1226 |
| avg_hold_time_bars | 40.3596 |
| exposure | 0.5815 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
