# EMA Hourly Continuation — TIA/USDT P26_34

**Symbol:** TIA/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1075 |
| net_profit_factor | 0.3951 |
| net_win_rate | 0.4112 |
| gross_profit_factor | 0.9041 |
| gross_win_rate | 0.4363 |
| sharpe_ratio | -10.8910 |
| sortino_ratio | -5.0749 |
| max_drawdown | 0.9986 |
| cagr | -0.9273 |
| net_avg_win | 14.7555 |
| net_avg_loss | -26.0792 |
| avg_hold_time_bars | 2.1014 |
| exposure | 0.1027 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
