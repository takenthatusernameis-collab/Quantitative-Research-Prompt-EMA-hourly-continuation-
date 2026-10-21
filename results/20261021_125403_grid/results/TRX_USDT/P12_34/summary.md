# EMA Hourly Continuation — TRX/USDT P12_34

**Symbol:** TRX/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.4453 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 1.0048 |
| gross_win_rate | 0.4908 |
| sharpe_ratio | -5.9904 |
| sortino_ratio | -1.9387 |
| max_drawdown | 0.8962 |
| cagr | -0.5931 |
| net_avg_win | 30.8542 |
| net_avg_loss | -63.5577 |
| avg_hold_time_bars | 7.7002 |
| exposure | 0.1705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
