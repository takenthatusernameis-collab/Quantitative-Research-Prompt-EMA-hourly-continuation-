# EMA Hourly Continuation — DOT/USDT P12_100

**Symbol:** DOT/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.6564 |
| net_win_rate | 0.4935 |
| gross_profit_factor | 0.9760 |
| gross_win_rate | 0.4954 |
| sharpe_ratio | -3.0633 |
| sortino_ratio | -1.0000 |
| max_drawdown | 0.7262 |
| cagr | -0.3841 |
| net_avg_win | 50.5442 |
| net_avg_loss | -75.0323 |
| avg_hold_time_bars | 26.1929 |
| exposure | 0.6417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
