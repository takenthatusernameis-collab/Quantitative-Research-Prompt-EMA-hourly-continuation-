# EMA Hourly Continuation — ACE/USDT P12_100

**Symbol:** ACE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7686 |
| net_win_rate | 0.4851 |
| gross_profit_factor | 0.9421 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -1.7788 |
| sortino_ratio | -0.5272 |
| max_drawdown | 0.4783 |
| cagr | -0.2155 |
| net_avg_win | 72.0556 |
| net_avg_loss | -88.3107 |
| avg_hold_time_bars | 29.2736 |
| exposure | 0.5763 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
