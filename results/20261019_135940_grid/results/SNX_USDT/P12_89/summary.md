# EMA Hourly Continuation — SNX/USDT P12_89

**Symbol:** SNX/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 797 |
| net_profit_factor | 0.6760 |
| net_win_rate | 0.4806 |
| gross_profit_factor | 1.0146 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -4.1664 |
| sortino_ratio | -1.6520 |
| max_drawdown | 0.8682 |
| cagr | -0.5458 |
| net_avg_win | 47.0313 |
| net_avg_loss | -64.3646 |
| avg_hold_time_bars | 14.0778 |
| exposure | 0.5077 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
