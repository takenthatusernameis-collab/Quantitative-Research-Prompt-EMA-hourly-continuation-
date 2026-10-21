# EMA Hourly Continuation — XDC/USDT P55_100

**Symbol:** XDC/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.6915 |
| net_win_rate | 0.5205 |
| gross_profit_factor | 1.0765 |
| gross_win_rate | 0.5205 |
| sharpe_ratio | -1.9746 |
| sortino_ratio | -0.5072 |
| max_drawdown | 0.4576 |
| cagr | -0.2060 |
| net_avg_win | 59.7351 |
| net_avg_loss | -93.7720 |
| avg_hold_time_bars | 7.9590 |
| exposure | 0.1147 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
