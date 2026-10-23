# EMA Hourly Continuation — BOME/USDT P12_100

**Symbol:** BOME/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 684 |
| net_profit_factor | 0.5992 |
| net_win_rate | 0.4635 |
| gross_profit_factor | 0.8252 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -3.7778 |
| sortino_ratio | -1.3886 |
| max_drawdown | 0.8264 |
| cagr | -0.4836 |
| net_avg_win | 38.1956 |
| net_avg_loss | -55.0578 |
| avg_hold_time_bars | 17.9137 |
| exposure | 0.5570 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
