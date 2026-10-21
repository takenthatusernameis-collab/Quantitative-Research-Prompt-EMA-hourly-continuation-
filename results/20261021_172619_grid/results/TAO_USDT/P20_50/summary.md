# EMA Hourly Continuation — TAO/USDT P20_50

**Symbol:** TAO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 472 |
| net_profit_factor | 0.8137 |
| net_win_rate | 0.5021 |
| gross_profit_factor | 1.0169 |
| gross_win_rate | 0.5021 |
| sharpe_ratio | -1.5077 |
| sortino_ratio | -0.4697 |
| max_drawdown | 0.4642 |
| cagr | -0.1954 |
| net_avg_win | 77.5446 |
| net_avg_loss | -96.1065 |
| avg_hold_time_bars | 7.5233 |
| exposure | 0.1614 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
