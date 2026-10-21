# EMA Hourly Continuation — ETH/USDT P34_200

**Symbol:** ETH/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 205 |
| net_profit_factor | 0.6758 |
| net_win_rate | 0.4878 |
| gross_profit_factor | 0.9281 |
| gross_win_rate | 0.4878 |
| sharpe_ratio | -1.6651 |
| sortino_ratio | -0.3407 |
| max_drawdown | 0.3429 |
| cagr | -0.1446 |
| net_avg_win | 67.6196 |
| net_avg_loss | -95.2978 |
| avg_hold_time_bars | 63.4585 |
| exposure | 0.5913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
