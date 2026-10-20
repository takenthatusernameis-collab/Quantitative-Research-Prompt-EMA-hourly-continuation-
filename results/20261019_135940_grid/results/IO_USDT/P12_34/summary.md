# EMA Hourly Continuation — IO/USDT P12_34

**Symbol:** IO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1212 |
| net_profit_factor | 0.6002 |
| net_win_rate | 0.4736 |
| gross_profit_factor | 0.9287 |
| gross_win_rate | 0.4843 |
| sharpe_ratio | -6.3877 |
| sortino_ratio | -3.2396 |
| max_drawdown | 0.9742 |
| cagr | -0.7881 |
| net_avg_win | 25.4846 |
| net_avg_loss | -38.1982 |
| avg_hold_time_bars | 4.1196 |
| exposure | 0.2417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
