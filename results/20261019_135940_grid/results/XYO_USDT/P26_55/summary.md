# EMA Hourly Continuation — XYO/USDT P26_55

**Symbol:** XYO/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1011 |
| net_profit_factor | 0.4066 |
| net_win_rate | 0.3887 |
| gross_profit_factor | 0.8126 |
| gross_win_rate | 0.4075 |
| sharpe_ratio | -10.4088 |
| sortino_ratio | -4.6876 |
| max_drawdown | 0.9975 |
| cagr | -0.9066 |
| net_avg_win | 17.3928 |
| net_avg_loss | -27.2008 |
| avg_hold_time_bars | 4.5361 |
| exposure | 0.2075 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
