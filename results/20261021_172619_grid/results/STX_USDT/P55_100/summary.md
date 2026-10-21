# EMA Hourly Continuation — STX/USDT P55_100

**Symbol:** STX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.6350 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.8350 |
| gross_win_rate | 0.4588 |
| sharpe_ratio | -2.5515 |
| sortino_ratio | -0.6686 |
| max_drawdown | 0.5423 |
| cagr | -0.2637 |
| net_avg_win | 60.0026 |
| net_avg_loss | -80.1095 |
| avg_hold_time_bars | 7.2529 |
| exposure | 0.1116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
