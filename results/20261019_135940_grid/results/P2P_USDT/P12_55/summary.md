# EMA Hourly Continuation — P2P/USDT P12_55

**Symbol:** P2P/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 971 |
| net_profit_factor | 0.3963 |
| net_win_rate | 0.3656 |
| gross_profit_factor | 0.5815 |
| gross_win_rate | 0.3656 |
| sharpe_ratio | -8.3664 |
| sortino_ratio | -3.6354 |
| max_drawdown | 0.9886 |
| cagr | -0.8319 |
| net_avg_win | 18.2814 |
| net_avg_loss | -26.5850 |
| avg_hold_time_bars | 8.7168 |
| exposure | 0.3847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
