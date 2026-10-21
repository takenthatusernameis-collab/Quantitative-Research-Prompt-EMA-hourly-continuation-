# EMA Hourly Continuation — BCH/USDT P26_34

**Symbol:** BCH/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 165 |
| net_profit_factor | 0.5896 |
| net_win_rate | 0.4788 |
| gross_profit_factor | 0.8962 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -2.0012 |
| sortino_ratio | -0.3693 |
| max_drawdown | 0.3543 |
| cagr | -0.1546 |
| net_avg_win | 62.5901 |
| net_avg_loss | -97.5088 |
| avg_hold_time_bars | 5.1697 |
| exposure | 0.0388 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
