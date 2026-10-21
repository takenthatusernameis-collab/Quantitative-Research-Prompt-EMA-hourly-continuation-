# EMA Hourly Continuation — JST/USDT P89_144

**Symbol:** JST/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.4842 |
| net_win_rate | 0.4846 |
| gross_profit_factor | 1.0026 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -3.5557 |
| sortino_ratio | -0.8714 |
| max_drawdown | 0.6548 |
| cagr | -0.3370 |
| net_avg_win | 42.6666 |
| net_avg_loss | -82.8683 |
| avg_hold_time_bars | 9.0887 |
| exposure | 0.1205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
