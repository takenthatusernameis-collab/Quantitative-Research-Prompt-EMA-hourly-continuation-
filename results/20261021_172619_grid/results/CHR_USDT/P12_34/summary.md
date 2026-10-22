# EMA Hourly Continuation — CHR/USDT P12_34

**Symbol:** CHR/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 702 |
| net_profit_factor | 0.6898 |
| net_win_rate | 0.4672 |
| gross_profit_factor | 0.9139 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -3.4853 |
| sortino_ratio | -1.3139 |
| max_drawdown | 0.7866 |
| cagr | -0.4527 |
| net_avg_win | 52.9889 |
| net_avg_loss | -67.3647 |
| avg_hold_time_bars | 6.9031 |
| exposure | 0.2193 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
