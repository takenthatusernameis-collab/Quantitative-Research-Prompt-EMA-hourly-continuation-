# EMA Hourly Continuation — WOO/USDT P8_55

**Symbol:** WOO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1037 |
| net_profit_factor | 0.6666 |
| net_win_rate | 0.4716 |
| gross_profit_factor | 1.0537 |
| gross_win_rate | 0.4851 |
| sharpe_ratio | -5.2747 |
| sortino_ratio | -2.3747 |
| max_drawdown | 0.9488 |
| cagr | -0.6830 |
| net_avg_win | 38.6120 |
| net_avg_loss | -51.6841 |
| avg_hold_time_bars | 10.3124 |
| exposure | 0.4861 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
