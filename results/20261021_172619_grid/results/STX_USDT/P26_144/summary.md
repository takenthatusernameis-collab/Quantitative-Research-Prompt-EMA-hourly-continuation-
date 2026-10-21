# EMA Hourly Continuation — STX/USDT P26_144

**Symbol:** STX/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 353 |
| net_profit_factor | 0.8691 |
| net_win_rate | 0.5156 |
| gross_profit_factor | 1.0524 |
| gross_win_rate | 0.5156 |
| sharpe_ratio | -0.7375 |
| sortino_ratio | -0.1987 |
| max_drawdown | 0.2949 |
| cagr | -0.0898 |
| net_avg_win | 77.0915 |
| net_avg_loss | -94.4127 |
| avg_hold_time_bars | 30.3768 |
| exposure | 0.4852 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
