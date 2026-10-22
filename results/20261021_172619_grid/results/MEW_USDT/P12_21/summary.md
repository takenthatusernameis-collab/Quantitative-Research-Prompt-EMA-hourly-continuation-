# EMA Hourly Continuation — MEW/USDT P12_21

**Symbol:** MEW/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 407 |
| net_profit_factor | 0.6735 |
| net_win_rate | 0.4693 |
| gross_profit_factor | 0.9115 |
| gross_win_rate | 0.4693 |
| sharpe_ratio | -2.8687 |
| sortino_ratio | -0.8271 |
| max_drawdown | 0.6556 |
| cagr | -0.3161 |
| net_avg_win | 66.4150 |
| net_avg_loss | -87.1956 |
| avg_hold_time_bars | 4.5799 |
| exposure | 0.0847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
