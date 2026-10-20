# EMA Hourly Continuation — XEC/USDT P12_144

**Symbol:** XEC/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.5863 |
| net_win_rate | 0.4580 |
| gross_profit_factor | 0.8998 |
| gross_win_rate | 0.4734 |
| sharpe_ratio | -4.1076 |
| sortino_ratio | -1.3925 |
| max_drawdown | 0.8242 |
| cagr | -0.4861 |
| net_avg_win | 43.1825 |
| net_avg_loss | -62.2310 |
| avg_hold_time_bars | 24.7118 |
| exposure | 0.6519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
