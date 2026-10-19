# EMA Hourly Continuation — ARB/USDT P12_50

**Symbol:** ARB/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1024 |
| net_profit_factor | 0.5063 |
| net_win_rate | 0.4746 |
| gross_profit_factor | 0.8827 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -5.7785 |
| sortino_ratio | -2.5988 |
| max_drawdown | 0.9591 |
| cagr | -0.7164 |
| net_avg_win | 20.2124 |
| net_avg_loss | -36.0615 |
| avg_hold_time_bars | 7.4902 |
| exposure | 0.3486 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
