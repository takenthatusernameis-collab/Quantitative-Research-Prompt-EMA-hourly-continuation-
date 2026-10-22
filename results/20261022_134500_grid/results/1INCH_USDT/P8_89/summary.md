# EMA Hourly Continuation — 1INCH/USDT P8_89

**Symbol:** 1INCH/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 697 |
| net_profit_factor | 0.5159 |
| net_win_rate | 0.4319 |
| gross_profit_factor | 0.8254 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -5.7758 |
| sortino_ratio | -2.1330 |
| max_drawdown | 0.9309 |
| cagr | -0.6485 |
| net_avg_win | 32.8474 |
| net_avg_loss | -48.3918 |
| avg_hold_time_bars | 20.6944 |
| exposure | 0.6556 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
