# EMA Hourly Continuation — TRADE/USDT P89_200

**Symbol:** TRADE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 310 |
| net_profit_factor | 0.4326 |
| net_win_rate | 0.3645 |
| gross_profit_factor | 0.5896 |
| gross_win_rate | 0.3645 |
| sharpe_ratio | -4.6851 |
| sortino_ratio | -1.1624 |
| max_drawdown | 0.7505 |
| cagr | -0.4238 |
| net_avg_win | 50.5789 |
| net_avg_loss | -67.0626 |
| avg_hold_time_bars | 13.2161 |
| exposure | 0.1862 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
