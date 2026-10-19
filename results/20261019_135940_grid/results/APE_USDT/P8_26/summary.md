# EMA Hourly Continuation — APE/USDT P8_26

**Symbol:** APE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1549 |
| net_profit_factor | 0.4075 |
| net_win_rate | 0.4416 |
| gross_profit_factor | 0.8445 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -9.9599 |
| sortino_ratio | -5.5252 |
| max_drawdown | 0.9989 |
| cagr | -0.9331 |
| net_avg_win | 10.0418 |
| net_avg_loss | -19.4883 |
| avg_hold_time_bars | 3.6139 |
| exposure | 0.2545 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
