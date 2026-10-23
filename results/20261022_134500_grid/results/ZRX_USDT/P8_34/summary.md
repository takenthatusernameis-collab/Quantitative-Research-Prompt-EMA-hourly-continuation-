# EMA Hourly Continuation — ZRX/USDT P8_34

**Symbol:** ZRX/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1342 |
| net_profit_factor | 0.4445 |
| net_win_rate | 0.4486 |
| gross_profit_factor | 0.8054 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -8.4217 |
| sortino_ratio | -4.3400 |
| max_drawdown | 0.9950 |
| cagr | -0.8788 |
| net_avg_win | 13.2271 |
| net_avg_loss | -24.2065 |
| avg_hold_time_bars | 5.9560 |
| exposure | 0.3633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
