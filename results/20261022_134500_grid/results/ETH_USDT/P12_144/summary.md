# EMA Hourly Continuation — ETH/USDT P12_144

**Symbol:** ETH/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 344 |
| net_profit_factor | 0.5304 |
| net_win_rate | 0.4680 |
| gross_profit_factor | 0.9096 |
| gross_win_rate | 0.4884 |
| sharpe_ratio | -3.4682 |
| sortino_ratio | -0.9033 |
| max_drawdown | 0.6902 |
| cagr | -0.3539 |
| net_avg_win | 46.7222 |
| net_avg_loss | -77.5021 |
| avg_hold_time_bars | 47.0669 |
| exposure | 0.7360 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
