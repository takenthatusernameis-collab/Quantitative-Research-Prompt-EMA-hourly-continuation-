# EMA Hourly Continuation — RPL/USDT P12_144

**Symbol:** RPL/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 423 |
| net_profit_factor | 0.8332 |
| net_win_rate | 0.5154 |
| gross_profit_factor | 1.0640 |
| gross_win_rate | 0.5177 |
| sharpe_ratio | -1.0627 |
| sortino_ratio | -0.3109 |
| max_drawdown | 0.3678 |
| cagr | -0.1378 |
| net_avg_win | 71.4969 |
| net_avg_loss | -91.2529 |
| avg_hold_time_bars | 37.4279 |
| exposure | 0.7165 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
