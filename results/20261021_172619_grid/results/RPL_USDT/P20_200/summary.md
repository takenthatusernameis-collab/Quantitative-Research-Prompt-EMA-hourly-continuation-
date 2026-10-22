# EMA Hourly Continuation — RPL/USDT P20_200

**Symbol:** RPL/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 287 |
| net_profit_factor | 0.9387 |
| net_win_rate | 0.5226 |
| gross_profit_factor | 1.0931 |
| gross_win_rate | 0.5226 |
| sharpe_ratio | -0.2909 |
| sortino_ratio | -0.0708 |
| max_drawdown | 0.1738 |
| cagr | -0.0360 |
| net_avg_win | 90.2111 |
| net_avg_loss | -105.2227 |
| avg_hold_time_bars | 52.8397 |
| exposure | 0.6863 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
