# EMA Hourly Continuation — BDX/USDT P34_144

**Symbol:** BDX/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1023 |
| net_profit_factor | 0.3091 |
| net_win_rate | 0.3109 |
| gross_profit_factor | 0.7386 |
| gross_win_rate | 0.3656 |
| sharpe_ratio | -14.5676 |
| sortino_ratio | -6.8189 |
| max_drawdown | 0.9999 |
| cagr | -0.9759 |
| net_avg_win | 14.0678 |
| net_avg_loss | -20.5286 |
| avg_hold_time_bars | 6.5758 |
| exposure | 0.3058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
