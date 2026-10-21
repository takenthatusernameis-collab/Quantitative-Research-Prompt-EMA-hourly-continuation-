# EMA Hourly Continuation — ZRX/USDT P26_100

**Symbol:** ZRX/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 490 |
| net_profit_factor | 0.7861 |
| net_win_rate | 0.5082 |
| gross_profit_factor | 1.0417 |
| gross_win_rate | 0.5082 |
| sharpe_ratio | -1.7555 |
| sortino_ratio | -0.5579 |
| max_drawdown | 0.5099 |
| cagr | -0.2259 |
| net_avg_win | 70.0015 |
| net_avg_loss | -92.0046 |
| avg_hold_time_bars | 15.8163 |
| exposure | 0.3523 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
