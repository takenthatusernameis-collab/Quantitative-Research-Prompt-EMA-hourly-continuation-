# EMA Hourly Continuation — YGG/USDT P34_200

**Symbol:** YGG/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 299 |
| net_profit_factor | 0.8612 |
| net_win_rate | 0.5050 |
| gross_profit_factor | 1.0098 |
| gross_win_rate | 0.5050 |
| sharpe_ratio | -0.7586 |
| sortino_ratio | -0.1876 |
| max_drawdown | 0.2557 |
| cagr | -0.0850 |
| net_avg_win | 82.4825 |
| net_avg_loss | -97.7135 |
| avg_hold_time_bars | 37.4816 |
| exposure | 0.5071 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
