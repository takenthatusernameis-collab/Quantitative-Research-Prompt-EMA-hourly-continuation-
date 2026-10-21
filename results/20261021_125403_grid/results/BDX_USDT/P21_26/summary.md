# EMA Hourly Continuation — BDX/USDT P21_26

**Symbol:** BDX/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 140 |
| net_profit_factor | 0.3493 |
| net_win_rate | 0.3429 |
| gross_profit_factor | 0.5724 |
| gross_win_rate | 0.3429 |
| sharpe_ratio | -3.9345 |
| sortino_ratio | -0.6696 |
| max_drawdown | 0.5667 |
| cagr | -0.2685 |
| net_avg_win | 60.8389 |
| net_avg_loss | -90.8680 |
| avg_hold_time_bars | 3.8429 |
| exposure | 0.0245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
