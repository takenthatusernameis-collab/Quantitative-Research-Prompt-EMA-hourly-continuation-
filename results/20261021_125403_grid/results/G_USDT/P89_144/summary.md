# EMA Hourly Continuation — G/USDT P89_144

**Symbol:** G/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 250 |
| net_profit_factor | 0.5853 |
| net_win_rate | 0.4640 |
| gross_profit_factor | 0.8566 |
| gross_win_rate | 0.4640 |
| sharpe_ratio | -2.7593 |
| sortino_ratio | -0.6714 |
| max_drawdown | 0.4998 |
| cagr | -0.2641 |
| net_avg_win | 59.1431 |
| net_avg_loss | -87.4719 |
| avg_hold_time_bars | 8.9720 |
| exposure | 0.1179 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
