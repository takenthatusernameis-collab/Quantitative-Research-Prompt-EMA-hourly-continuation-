# EMA Hourly Continuation — BDX/USDT P21_55

**Symbol:** BDX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1352 |
| net_profit_factor | 0.2627 |
| net_win_rate | 0.2641 |
| gross_profit_factor | 0.6640 |
| gross_win_rate | 0.3299 |
| sharpe_ratio | -19.8057 |
| sortino_ratio | -11.1005 |
| max_drawdown | 1.0000 |
| cagr | -0.9980 |
| net_avg_win | 9.9816 |
| net_avg_loss | -13.6316 |
| avg_hold_time_bars | 3.8706 |
| exposure | 0.2379 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
