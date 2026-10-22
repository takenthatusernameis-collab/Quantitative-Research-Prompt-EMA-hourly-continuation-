# EMA Hourly Continuation — UMA/USDT P21_144

**Symbol:** UMA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.6956 |
| net_win_rate | 0.4715 |
| gross_profit_factor | 0.8770 |
| gross_win_rate | 0.4715 |
| sharpe_ratio | -2.3022 |
| sortino_ratio | -0.6839 |
| max_drawdown | 0.5643 |
| cagr | -0.2716 |
| net_avg_win | 60.5779 |
| net_avg_loss | -77.7079 |
| avg_hold_time_bars | 24.9157 |
| exposure | 0.4972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
